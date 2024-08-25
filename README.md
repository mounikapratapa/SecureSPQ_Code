# Similar-Patient-Query
Dataset link: The dataset used in this code is randomly generated to test the code for robustness. However, this code works for any type of SNP data. 

The code provided in this repository is for demonstrating a working example of [Our paper on secure SPQ](https://doi.org/10.1016/j.jisa.2024.103861)

Use the qr-keygen to generate the required primes. These primes enable us to evaluate the sign function appropriately. Encrypt your hospital database records using the paper's OU encryption scheme and algorithm 1. 

Use spq_user to perform secure Euclidean distance computation and secure function evaluation. 

The hosp_dec will decrypt and evaluate similarity securely without displaying the results. This file only outputs the output of QR function, it needs modification for exchanging similar patient records by appropriate indexing. 

LSH results are computed on plaintext data for simplicity. In encryption, the hashcode indexes directly point to the encrypted vectors. Since HE offers 100 % accuracy, it is expected to behave similarly. The LSH example was provided for demonstration purpose only and it is not secure. 

Requirements:
- Python 3.x 
No additional libraries or packages are required. This implementation is built entirely from scratch using only Python standard libraries.



