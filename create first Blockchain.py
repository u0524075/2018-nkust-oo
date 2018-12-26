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
    "from time import time\n",
    "\n",
    "\n",
    "class Blockchain(object):\n",
    "    def __init__(self):\n",
    "        self.current_transactions = []\n",
    "        self.chain = []\n",
    "\n",
    "        # Create the genesis block\n",
    "        self.new_block(previous_hash=1, proof=100)\n",
    "\n",
    "    def new_block(self, proof, previous_hash=None):\n",
    "\n",
    "        block = {\n",
    "            'index': len(self.chain) + 1,\n",
    "            'timestamp': time(),\n",
    "            'transactions': self.current_transactions,\n",
    "            'proof': proof,\n",
    "            'previous_hash': previous_hash or self.hash(self.chain[-1]),\n",
    "        }\n",
    "\n",
    "        # Reset the current list of transactions\n",
    "        self.current_transactions = []\n",
    "\n",
    "        self.chain.append(block)\n",
    "        return block\n",
    "\n",
    "    def new_transaction(self, sender, recipient, amount):\n",
    "        \n",
    "        self.current_transactions.append({\n",
    "            'sender': sender,\n",
    "            'recipient': recipient,\n",
    "            'amount': amount,\n",
    "        })\n",
    "\n",
    "        return self.last_block['index'] + 1\n",
    "\n",
    "    @property\n",
    "    def last_block(self):\n",
    "        return self.chain[-1]\n",
    "\n",
    "    @staticmethod\n",
    "    def hash(block):\n",
    "      \n",
    "        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes\n",
    "        block_string = json.dumps(block, sort_keys=True).encode()\n",
    "        return hashlib.sha256(block_string).hexdigest()\n",
    "\n"
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
