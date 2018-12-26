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
    "\n",
    "from time import time\n",
    "from uuid import uuid4\n",
    "\n",
    "from flask import Flask, jsonify, request\n",
    "\n",
    "...\n",
    "\n",
    "@app.route('/mine', methods=['GET'])\n",
    "def mine():\n",
    "    # We run the proof of work algorithm to get the next proof...\n",
    "    last_block = blockchain.last_block\n",
    "    last_proof = last_block['proof']\n",
    "    proof = blockchain.proof_of_work(last_proof)\n",
    "\n",
    "    # 給獎勵.\n",
    "    # “0”為新挖出的幣\n",
    "    blockchain.new_transaction(\n",
    "        sender=\"0\",\n",
    "        recipient=node_identifier,\n",
    "        amount=1,\n",
    "    )\n",
    "\n",
    "    # Forge the new Block by adding it to the chain\n",
    "    block = blockchain.new_block(proof)\n",
    "\n",
    "    response = {\n",
    "        'message': \"New Block Forged\",\n",
    "        'index': block['index'],\n",
    "        'transactions': block['transactions'],\n",
    "        'proof': block['proof'],\n",
    "        'previous_hash': block['previous_hash'],\n",
    "    }\n",
    "    return jsonify(response), 200\n",
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
