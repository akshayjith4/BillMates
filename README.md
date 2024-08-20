<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BillMates - README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f4f4f4;
            padding: 20px;
        }
        h1 {
            color: #2c3e50;
        }
        h2 {
            color: #16a085;
            border-bottom: 2px solid #16a085;
            padding-bottom: 5px;
        }
        ul, ol {
            margin: 20px 0;
            padding-left: 20px;
        }
        code {
            background-color: #ecf0f1;
            padding: 2px 4px;
            border-radius: 4px;
        }
        pre {
            background-color: #ecf0f1;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        a {
            color: #2980b9;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>

    <h1>BillMates</h1>

    <p><strong>BillMates</strong> is a user-friendly app designed to simplify managing shared expenses among flatmates. Keep track of bills, split costs fairly, and ensure everyone knows what they owe.</p>

    <h2>Features</h2>
    <ul>
        <li><strong>Bill Tracking</strong>: Easily add and track shared expenses.</li>
        <li><strong>Expense Splitting</strong>: Automatically calculate each flatmate's share of the expenses.</li>
        <li><strong>Payment Reminders</strong>: Get notifications for upcoming payments and reminders for due bills.</li>
        <li><strong>Expense History</strong>: View past expenses and payment history for transparency.</li>
        <li><strong>User-Friendly Interface</strong>: Simple and intuitive design for easy navigation.</li>
    </ul>

    <h2>Installation</h2>
    <p>To install and run the BillMates app locally, follow these steps:</p>

    <h3>Prerequisites</h3>
    <ul>
        <li>Python 3.6+</li>
        <li>pip (Python package installer)</li>
    </ul>

    <h3>Steps</h3>
    <ol>
        <li><strong>Clone the Repository</strong>:
            <pre><code>git clone https://github.com/akshayjith4/billmates.git<br>cd billmates</code></pre>
        </li>
        <li><strong>Create a Virtual Environment</strong>:
            <pre><code>python -m venv venv<br>source venv/bin/activate  # On Windows, use `venv\Scripts\activate`</code></pre>
        </li>
        <li><strong>Install Dependencies</strong>:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li><strong>Run the Application</strong>:
            <pre><code>python app.py</code></pre>
        </li>
    </ol>

    <h2>Usage</h2>
    <ul>
        <li><strong>Sign Up/Log In</strong>: Create a new account or log in with your existing credentials.</li>
        <li><strong>Add Flatmates</strong>: Add your flatmates to the app.</li>
        <li><strong>Add Expenses</strong>: Enter details of shared expenses, such as rent, utilities, and groceries.</li>
        <li><strong>Split Costs</strong>: The app automatically calculates and splits costs among the flatmates.</li>
        <li><strong>View Balances</strong>: Check each flatmate's balance to see who owes what.</li>
        <li><strong>Settle Up</strong>: Record payments when flatmates settle their balances.</li>
    </ul>

    <h2>Online Access</h2>
    <p>BillMates is also available online at <a href="http://Akshayjith.pythonanywhere.com">BillMates</a>. The site will be available for only 3 months because, let's face it, domains are expensive and this is a passion project.</p>

    <h2>We welcome contributions!</h2>

</body>
</html>
