{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import hashlib\n",
    "import json\n",
    "from textwrap import dedent\n",
    "from time import time\n",
    "from uuid import uuid4\n",
    "\n",
    "from flask import Flask\n",
    "\n",
    "\n",
    "class Blockchain(object):\n",
    "    ...\n",
    "\n",
    "\n",
    "# Instantiate our Node\n",
    "app = Flask(__name__)\n",
    "\n",
    "# Generate a globally unique address for this node\n",
    "node_identifier = str(uuid4()).replace('-', '')\n",
    "\n",
    "# Instantiate the Blockchain\n",
    "blockchain = Blockchain()\n",
    "\n",
    "\n",
    "@app.route('/mine', methods=['GET'])\n",
    "def mine():\n",
    "    return \"We'll mine a new Block\"\n",
    "  \n",
    "@app.route('/transactions/new', methods=['POST'])\n",
    "def new_transaction():\n",
    "    return \"We'll add a new transaction\"\n",
    "\n",
    "@app.route('/chain', methods=['GET'])\n",
    "def full_chain():\n",
    "    response = {\n",
    "        'chain': blockchain.chain,\n",
    "        'length': len(blockchain.chain),\n",
    "    }\n",
    "    return jsonify(response), 200\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(host='0.0.0.0', port=5000)\n",
    "\n",
    "{\n",
    " \"sender\": \"my address\",\n",
    " \"recipient\": \"someone else's address\",\n",
    " \"amount\": 5\n",
    "}"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.6.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
