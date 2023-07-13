from bs4 import BeautifulSoup
import random

# Original HTML table
html_table = '''
      <table class="transactions">
        <tr>
          <th>Date</th>
          <th>Type</th>
          <th>Merchant</th>
          <th>Amount</th>
        </tr>
        <tr class="transaction-row">
          <td class="transaction-date">109</td>
          <td class="transaction-type">Withdrawal</td>
          <td class="transaction-merchant">ATM</td>
          <td class="transaction-amount">$250.00</td>
        </tr>
        <tr class="transaction-row">
          <td class="transaction-date">123</td>
          <td class="transaction-type">Fee</td>
          <td class="transaction-merchant">N/A</td>
          <td class="transaction-amount">$25.00</td>
        </tr>
        <tr class="transaction-row">
          <td class="transaction-date">124</td>
          <td class="transaction-type">Purchase</td>
          <td class="transaction-merchant">Gamestop</td>
          <td class="transaction-amount">$59.99</td>
        </tr>
        <tr class="transaction-row">
          <td class="transaction-date">125</td>
          <td class="transaction-type">Purchase</td>
          <td class="transaction-merchant">Deli on Broadway</td>
          <td class="transaction-amount">$18.41</td>
        </tr>
        <tr class="transaction-row">
          <td class="transaction-date">132</td>
          <td class="transaction-type">Purchase</td>
          <td class="transaction-merchant">CVS</td>
          <td class="transaction-amount">$1.89</td>
        </tr>
        <tr class="transaction-row">
          <td class="transaction-date">154</td>
          <td class="transaction-type">Refund</td>
          <td class="transaction-merchant">Gamestop</td>
          <td class="transaction-amount">-$59.99</td>
        </tr>
      </table>
'''

# Generate additional transactions
additional_transactions = ''
soup = BeautifulSoup(html_table, 'html.parser')
transaction_rows = soup.find_all('tr', class_='transaction-row')

for i in range(155, 450):
    t_type = random.choice(["Purchase", "Refund", "Fee", "Withdrawal"])
    negative_character = ""

    if t_type == "Refund":
        negative_character = "-"

    additional_transactions += f'''
    <tr class="transaction-row">
        <td class="transaction-date">{i}</td>
        <td class="transaction-type">{t_type}</td>
        <td class="transaction-merchant">Merchant{i}</td>
        <td class="transaction-amount">{negative_character}${i}.00</td>
    </tr>
    '''

# Append additional transactions to the original table
updated_table = soup.find('table', class_='transactions')
updated_table.append(BeautifulSoup(additional_transactions, 'html.parser'))

# Print the updated HTML table
print(updated_table.prettify())

