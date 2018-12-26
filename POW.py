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
    "\n",
    "class Blockchain(object):\n",
    "    ...\n",
    "        \n",
    "    def proof_of_work(self, last_proof):\n",
    "\n",
    "        proof = 0\n",
    "        while self.valid_proof(last_proof, proof) is False:\n",
    "            proof += 1\n",
    "\n",
    "        return proof\n",
    "\n",
    "    @staticmethod\n",
    "    def valid_proof(last_proof, proof):\n",
    "    \n",
    "        guess = f'{last_proof}{proof}'.encode()\n",
    "        guess_hash = hashlib.sha256(guess).hexdigest()\n",
    "        return guess_hash[:4] == \"0000\"\n"
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
