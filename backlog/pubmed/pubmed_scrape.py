from Bio import Entrez

def fetch_pubmed_records(email, search_term, max_records=100):
    """
    Fetch PubMed records matching the search term.

    Parameters:
        email (str): Email address for NCBI.
        search_term (str): The term to search for in PubMed.
        max_records (int): Maximum number of records to fetch.

    Returns:
        list: List of PubMed IDs (PMIDs).
    """
    Entrez.email = email
    handle = Entrez.esearch(db="pubmed", term=search_term, retmax=max_records)
    record = Entrez.read(handle)
    handle.close()
    id_list = record["IdList"]
    return id_list

def fetch_pubmed_details(id_list):
    """
    Fetch detailed information for a list of PubMed IDs.

    Parameters:
        id_list (list): List of PubMed IDs.

    Returns:
        dict: Parsed XML data with detailed information for each PubMed ID.
    """
    ids = ",".join(id_list)
    handle = Entrez.efetch(db="pubmed", id=ids, rettype="xml", retmode="xml")
    data = Entrez.read(handle)  # Read the data using Entrez.read
    handle.close()
    return data

def extract_pubmed_info(records):
    """
    Extract required information from PubMed records.

    Parameters:
        records (dict): Parsed XML data from PubMed.

    Returns:
        list: List of dictionaries with extracted information.
    """
    extracted_data = []
    for record in records['PubmedArticle']:
        medline_citation = record.get('MedlineCitation', {})
        article = medline_citation.get('Article', {})
        journal = article.get('Journal', {})
        journal_issue = journal.get('JournalIssue', {})
        pub_date = journal_issue.get('PubDate', {})
        
        # Extract article information
        article_info = {
            "Title": article.get("ArticleTitle", ""),
            "Abstract": ' '.join(article.get("Abstract", {}).get("AbstractText", [])),
            "PublicationDate": pub_date.get("Year", ""),
            "Authors": [f"{author.get('LastName', '')} {author.get('ForeName', '')}" for author in article.get("AuthorList", [])],
            "Journal": journal.get("Title", ""),
            "PMID": medline_citation.get("PMID", ""),
        }
        extracted_data.append(article_info)
    return extracted_data

def main():
    """
    Main function to fetch, parse, and print PubMed data.
    """
    email = "your_email@example.com"  # Replace with your email
    search_term = "COVID-19"  # Replace with your search term
    max_records = 100  # Adjust the number of records to fetch

    print("Fetching PubMed records...")
    id_list = fetch_pubmed_records(email, search_term, max_records)
    
    print(f"Found {len(id_list)} records. Fetching details...")
    records = fetch_pubmed_details(id_list)

    print("Extracting information from records...")
    extracted_data = extract_pubmed_info(records)
    
    # Print or save the extracted data
    for data in extracted_data:
        print(f"PMID: {data['PMID']}")
        print(f"Title: {data['Title']}")
        print(f"Abstract: {data['Abstract']}")
        print(f"Publication Date: {data['PublicationDate']}")
        print(f"Authors: {', '.join(data['Authors'])}")
        print(f"Journal: {data['Journal']}")
        print("\n")

if __name__ == "__main__":
    main()
