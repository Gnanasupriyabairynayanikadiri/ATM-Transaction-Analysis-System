{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "0251c3fe-9ccd-4d08-862e-666674b74f66",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "------Main Menu------\n",
      "\n",
      "1.Register\n",
      "2.Login\n",
      "3.Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  1\n",
      "Enter Account Number:  2837465\n",
      "Set 4-digit pin:  ········\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Account Created Successfully\n",
      "\n",
      "\n",
      "------Main Menu------\n",
      "\n",
      "1.Register\n",
      "2.Login\n",
      "3.Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  2\n",
      "Enter Account Number:  2837465\n",
      "Enter Pin:  ········\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Login Successfully!\n",
      "\n",
      "\n",
      "------atm_menu---------\n",
      "\n",
      "1.Check balance\n",
      "2.Deposit\n",
      "3.Withdraw\n",
      "4.Transaction history\n",
      "5.Mini Statement\n",
      "6.Change pin\n",
      "7.Analyze Transactions\n",
      "8.Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Choose Option:  1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Balance: 0\n",
      "\n",
      "------atm_menu---------\n",
      "\n",
      "1.Check balance\n",
      "2.Deposit\n",
      "3.Withdraw\n",
      "4.Transaction history\n",
      "5.Mini Statement\n",
      "6.Change pin\n",
      "7.Analyze Transactions\n",
      "8.Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Choose Option:  2\n",
      "Enter deposit amount:  100000\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Deposit Successful!\n",
      "\n",
      "------atm_menu---------\n",
      "\n",
      "1.Check balance\n",
      "2.Deposit\n",
      "3.Withdraw\n",
      "4.Transaction history\n",
      "5.Mini Statement\n",
      "6.Change pin\n",
      "7.Analyze Transactions\n",
      "8.Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Choose Option:  3\n",
      "Enter Withdrawal amount:  25000\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Withdrawal Succeessful!\n",
      "\n",
      "------atm_menu---------\n",
      "\n",
      "1.Check balance\n",
      "2.Deposit\n",
      "3.Withdraw\n",
      "4.Transaction history\n",
      "5.Mini Statement\n",
      "6.Change pin\n",
      "7.Analyze Transactions\n",
      "8.Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Choose Option:  4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "------Transaction History------\n",
      "\n",
      "1. 03-03-2026 14:52:15 - Deposit - 100000.0\n",
      "2. 03-03-2026 14:52:21 - Withdrew - 25000.0\n",
      "-------------------------------\n",
      "\n",
      "\n",
      "------atm_menu---------\n",
      "\n",
      "1.Check balance\n",
      "2.Deposit\n",
      "3.Withdraw\n",
      "4.Transaction history\n",
      "5.Mini Statement\n",
      "6.Change pin\n",
      "7.Analyze Transactions\n",
      "8.Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Choose Option:  5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "--Mini Statement(Last 5 Transactions)--\n",
      "\n",
      "1. 03-03-2026 14:52:15 - Deposit - 100000.0\n",
      "2. 03-03-2026 14:52:21 - Withdrew - 25000.0\n",
      "\n",
      "------------------------\n",
      "\n",
      "\n",
      "------atm_menu---------\n",
      "\n",
      "1.Check balance\n",
      "2.Deposit\n",
      "3.Withdraw\n",
      "4.Transaction history\n",
      "5.Mini Statement\n",
      "6.Change pin\n",
      "7.Analyze Transactions\n",
      "8.Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Choose Option:  6\n",
      "Enter Account Number:  2837465\n",
      "Enter Old Pin:  ········\n",
      "Enter New Pin:  ········\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pin Changed Successfully\n",
      "\n",
      "\n",
      "------atm_menu---------\n",
      "\n",
      "1.Check balance\n",
      "2.Deposit\n",
      "3.Withdraw\n",
      "4.Transaction history\n",
      "5.Mini Statement\n",
      "6.Change pin\n",
      "7.Analyze Transactions\n",
      "8.Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Choose Option:  7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "------Transaction Data------\n",
      "\n",
      "       type    amount                time\n",
      "0   Deposit  100000.0 2026-03-03 14:52:15\n",
      "1  Withdrew   25000.0 2026-03-03 14:52:21\n",
      "----Summary----\n",
      "\n",
      "Total Deposited: ₹ 100000.0\n",
      "Total Withdrawn: ₹ 0.0\n",
      "\n",
      "------ Monthly Summary ------\n",
      "month    type    \n",
      "2026-03  Deposit     100000.0\n",
      "         Withdrew     25000.0\n",
      "Name: amount, dtype: float64\n",
      "\n",
      "------atm_menu---------\n",
      "\n",
      "1.Check balance\n",
      "2.Deposit\n",
      "3.Withdraw\n",
      "4.Transaction history\n",
      "5.Mini Statement\n",
      "6.Change pin\n",
      "7.Analyze Transactions\n",
      "8.Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Choose Option:  8\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Thank you for using ATM\n",
      "\n",
      "\n",
      "------Main Menu------\n",
      "\n",
      "1.Register\n",
      "2.Login\n",
      "3.Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Exiting Program!\n"
     ]
    }
   ],
   "source": [
    "# ATM Login System \n",
    "import pandas as pd\n",
    "import getpass\n",
    "from datetime import datetime\n",
    "\n",
    "accounts = {}\n",
    "\n",
    "#Register\n",
    "def register():\n",
    "    account_number = input(\"Enter Account Number: \")\n",
    "\n",
    "    if account_number in accounts:\n",
    "        print(\"Account already exists!\")\n",
    "        return\n",
    "\n",
    "    pin = getpass.getpass(\"Set 4-digit pin: \")\n",
    "\n",
    "    if len(pin) != 4 or not pin.isdigit():\n",
    "        print(\"Invalid pin! Must contain 4-digits.\")\n",
    "        return\n",
    "\n",
    "    accounts[account_number] = {\"pin\": pin, \"balance\": 0, \"history\": []}\n",
    "    print(\"Account Created Successfully\\n\")\n",
    "\n",
    "#Login\n",
    "#attempts = 3\n",
    "\n",
    "def login():\n",
    "    attempts = 3\n",
    "    while attempts > 0:\n",
    "        account_number = input(\"Enter Account Number: \")\n",
    "        pin = getpass.getpass(\"Enter Pin: \")\n",
    "    \n",
    "        if account_number in accounts and accounts[account_number][\"pin\"] == pin:\n",
    "            print(\"Login Successfully!\\n\")\n",
    "            atm_menu(account_number)\n",
    "            break\n",
    "        else:\n",
    "            attempts -= 1\n",
    "            print(\"Invalid Credential!\")\n",
    "            print(\"Attempts left\", attempts)\n",
    "            \n",
    "    if attempts == 0:\n",
    "        print(\"Account Locked\")\n",
    "\n",
    "#Change ATM Pin\n",
    "def change_pin(account_number):\n",
    "    \n",
    "\n",
    "    old_pin = getpass.getpass(\"Enter Old Pin: \")\n",
    "\n",
    "    if accounts[account_number][\"pin\"] == old_pin:\n",
    "\n",
    "        new_pin = getpass.getpass(\"Enter New Pin: \")\n",
    "\n",
    "        if len(new_pin) == 4 and new_pin.isdigit():\n",
    "            accounts[account_number][\"pin\"] = new_pin\n",
    "            print(\"Pin Changed Successfully\\n\")\n",
    "        else:\n",
    "            print(\"Pin must contain 4 digits only\")\n",
    "\n",
    "    else:\n",
    "        print(\"Incorrect Old Pin\\n\")\n",
    "#Analysis Function\n",
    "def analyze_transaction(account_number):\n",
    "    history = accounts[account_number][\"history\"]\n",
    "\n",
    "    if not history:\n",
    "        print(\"No transactions to analyze.\")\n",
    "        return\n",
    "\n",
    "    #Convert list of dictionaries to dataframe\n",
    "    df = pd.DataFrame(history)\n",
    "\n",
    "    #Convert time column to datetime\n",
    "    df[\"time\"] = pd.to_datetime(df[\"time\"], format = \"%d-%m-%Y %H:%M:%S\")\n",
    "\n",
    "    print(\"\\n------Transaction Data------\\n\")\n",
    "    print(df)\n",
    "\n",
    "    #Total Deposits\n",
    "    total_deposit = df[df[\"type\"] == \"Deposit\"][\"amount\"].sum()\n",
    "\n",
    "    #Total Withdrawals \n",
    "    total_withdraw = df[df[\"type\"] == \"Withdraw\"][\"amount\"].sum()\n",
    "\n",
    "    print(\"----Summary----\\n\")\n",
    "    print(\"Total Deposited: ₹\", total_deposit)\n",
    "    print(\"Total Withdrawn: ₹\", total_withdraw)\n",
    "\n",
    "     # Monthly Summary\n",
    "    df[\"month\"] = df[\"time\"].dt.to_period(\"M\")\n",
    "\n",
    "    monthly_summary = df.groupby([\"month\", \"type\"])[\"amount\"].sum()\n",
    "\n",
    "    print(\"\\n------ Monthly Summary ------\")\n",
    "    print(monthly_summary)\n",
    "\n",
    "\n",
    "\n",
    "#ATM Menu\n",
    "def atm_menu(account_number):\n",
    "    while True:\n",
    "        print(\"\\n------atm_menu---------\\n\")\n",
    "        print(\"1.Check balance\")\n",
    "        print(\"2.Deposit\")\n",
    "        print(\"3.Withdraw\")\n",
    "        print(\"4.Transaction history\")\n",
    "        print(\"5.Mini Statement\")\n",
    "        print(\"6.Change pin\")\n",
    "        print(\"7.Analyze Transactions\")\n",
    "        print(\"8.Exit\")\n",
    "\n",
    "        choice = input(\"Choose Option: \")\n",
    "\n",
    "        if choice == \"1\":\n",
    "            print(\"Balance:\", accounts[account_number][\"balance\"])\n",
    "        elif choice == \"2\":\n",
    "            amount = float(input(\"Enter deposit amount: \"))\n",
    "            accounts[account_number][\"balance\"] += amount\n",
    "\n",
    "            now = datetime.now()\n",
    "            time_stamp = now.strftime(\"%d-%m-%Y %H:%M:%S\")\n",
    "\n",
    "            #Add transaction record\n",
    "            accounts[account_number][\"history\"].append({\"type\": \"Deposit\", \"amount\": amount, \"time\": time_stamp})\n",
    "\n",
    "            print(\"Deposit Successful!\")\n",
    "\n",
    "        elif choice == \"3\":\n",
    "            amount = float(input(\"Enter Withdrawal amount: \"))\n",
    "            if amount <= accounts[account_number][\"balance\"]:\n",
    "                accounts[account_number][\"balance\"] -= amount\n",
    "                now = datetime.now()\n",
    "                time_stamp = now.strftime(\"%d-%m-%Y %H:%M:%S\")\n",
    "\n",
    "                #Add transaction record\n",
    "                accounts[account_number][\"history\"].append({\"type\": \"Withdrew\", \"amount\": amount, \"time\": time_stamp})\n",
    "                print(\"Withdrawal Succeessful!\")\n",
    "            else:\n",
    "                print(\"Insufficient balance!\")\n",
    "\n",
    "        elif choice == \"4\":\n",
    "            print(\"\\n------Transaction History------\\n\")\n",
    "            history = accounts[account_number][\"history\"]\n",
    "\n",
    "            if not history:\n",
    "                print(\"No transactions yet.\")\n",
    "            else:\n",
    "                for i, transaction in enumerate(history, start = 1):\n",
    "                    print(f\"{i}. {transaction['time']} - {transaction['type']} - {transaction['amount']}\")\n",
    "            print(\"-------------------------------\\n\")\n",
    "\n",
    "        elif choice == \"5\":\n",
    "            print(\"\\n--Mini Statement(Last 5 Transactions)--\\n\")\n",
    "\n",
    "            history = accounts[account_number][\"history\"]\n",
    "\n",
    "            if not history:\n",
    "                print(\"No transactions yet.\")\n",
    "            else:\n",
    "                last_five = history[-5:]\n",
    "\n",
    "                for i, transaction in enumerate(last_five, start = 1):\n",
    "                    print(f\"{i}. {transaction['time']} - {transaction['type']} - {transaction['amount']}\")\n",
    "                print(\"\\n------------------------\\n\")\n",
    "\n",
    "        elif choice == \"6\":\n",
    "                change_pin(account_number)\n",
    "\n",
    "        elif choice == \"7\":\n",
    "            analyze_transaction(account_number)\n",
    "            \n",
    "                \n",
    "        elif choice == \"8\":\n",
    "                print(\"Thank you for using ATM\\n\")\n",
    "                break\n",
    "        else:\n",
    "                print(\"Invalid Option\")\n",
    "        \n",
    "\n",
    "#Main menu\n",
    "while True:\n",
    "    print(\"\\n------Main Menu------\\n\")\n",
    "    print(\"1.Register\")\n",
    "    print(\"2.Login\")\n",
    "    print(\"3.Exit\")\n",
    "\n",
    "    choice = input(\"Enter your choice: \")\n",
    "\n",
    "    if choice == \"1\":\n",
    "        register()\n",
    "    elif choice == \"2\":\n",
    "        login()\n",
    "    elif choice == \"3\":\n",
    "        print(\"Exiting Program!\")\n",
    "        break\n",
    "    else:\n",
    "        print(\"Invalid Choice!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3a2ce5ee-b7c9-4d36-8a3b-566316468fbd",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "afb524dd-d10e-4597-bd51-f23f6d8f8e7f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "04d55eb1-791f-4ce2-b169-9511005c10e8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
