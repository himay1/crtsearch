import requests
import csv
import argparse

def fetch_crtsh_data(domain):
    url = f'https://crt.sh/?q=%25.{domain}&output=json'
    response = requests.get(url)
    data = response.json()
    return data

def save_to_csv(data, domain):
    csv_filename = f'{domain}_certificates.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['common_name', 'Matching_Identities', 'issuer_name', 'not_before', 'not_after']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for entry in data:
            writer.writerow({
                'common_name': entry['common_name'],
                'Matching_Identities': entry['name_value'],
                'issuer_name': entry['issuer_name'],
                'not_before': entry['not_before'],
                'not_after': entry['not_after']
            })
    return {'domain': domain, 'csv_filename': csv_filename}

def main():
    parser = argparse.ArgumentParser(description='Fetch SSL certificate information from crt.sh')
    parser.add_argument('-t', '--domain', help='Single domain name to query for SSL certificates')
    parser.add_argument('-T', '--txtfile', help='Text file containing a list of domains to query')
    args = parser.parse_args()

    if args.domain:
        domains = [args.domain]
    elif args.txtfile:
        with open(args.txtfile, 'r') as file:
            domains = [line.strip() for line in file.readlines()]
    else:
        parser.error('Please provide either a single domain using -t or a text file containing domains using -T')

    all_results = []

    for domain in domains:
        data = fetch_crtsh_data(domain)
        result = save_to_csv(data, domain)
        all_results.append(result)
        print(f'Certificate information for {domain} has been saved to {result["csv_filename"]}')

    # Generate a CSV file containing all results
    if args.txtfile:  # Only generate 'all_results.csv' if a text file is provided
        all_csv_filename = 'all_results.csv'
        with open(all_csv_filename, 'w', newline='') as csvfile:
            fieldnames = ['domain', 'csv_filename', 'common_name', 'Matching_Identities', 'issuer_name', 'not_before', 'not_after']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for result in all_results:
                domain = result['domain']
                csv_filename = result['csv_filename']
                with open(csv_filename, 'r') as individual_csv:
                    reader = csv.DictReader(individual_csv)
                    for row in reader:
                        writer.writerow({
                            'domain': domain,
                            'csv_filename': csv_filename,
                            'common_name': row['common_name'],
                            'Matching_Identities': row['Matching_Identities'],
                            'issuer_name': row['issuer_name'],
                            'not_before': row['not_before'],
                            'not_after': row['not_after']
                        })

        print(f'All results have been saved to {all_csv_filename}')

if __name__ == '__main__':
    main()
