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
    "\n",
    "from urllib.parse import urlparse\n",
    "\n",
    "\n",
    "\n",
    "class Blockchain(object):\n",
    "    def __init__(self):\n",
    "        ...\n",
    "        self.nodes = set()\n",
    "        ...\n",
    "\n",
    "    def register_node(self, address):\n",
    "        \"\"\"\n",
    "        Add a new node to the list of nodes\n",
    "        :param address: <str> Address of node. Eg. 'http://192.168.0.5:5000'\n",
    "        :return: None\n",
    "        \"\"\"\n",
    "\n",
    "        parsed_url = urlparse(address)\n",
    "        self.nodes.add(parsed_url.netloc)\n"
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
