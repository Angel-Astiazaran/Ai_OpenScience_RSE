# Rationale for Result Validation

This document explains how we have validated each of the results obtained from our analysis of 10 open-access articles using Grobid.

## 1️⃣ Keyword Cloud Validation  
**Objective:** Generate a word cloud based on the abstracts of the papers.  

### 🔍 Validation Method:  
- Manually reviewed extracted abstracts to ensure they were correctly parsed.  
- Verified that the word cloud contains relevant keywords from the abstracts.  
- Compared word frequencies with a manual count of common words in the abstracts.  

### ✅ Validation Steps:  
1. Extracted abstracts were saved to a text file (`results/abstracts.txt`).  
2. A script was run to count word occurrences and generate the word cloud.  
3. A manual check was performed to verify that high-frequency words appeared prominently in the word cloud.  
4. Tested with different subsets of abstracts to confirm consistency.  

---

## 2️⃣ Figure Count Validation  
**Objective:** Count and visualize the number of figures per article.  

### 🔍 Validation Method:  
- Manually checked the number of figures in the PDFs.  
- Compared manual count with the output of our script.  
- Tested the script on known cases with a specific number of figures.  

### ✅ Validation Steps:  
1. Extracted figure counts were saved to `results/figures_count.json`.  
2. Randomly selected 3 articles and manually counted the figures.  
3. Compared manual counts with the output of the script.  
4. Verified that the visualization accurately represented the extracted data.  

---

## 3️⃣ Link Extraction Validation  
**Objective:** Extract and list all URLs found in the papers.  

### 🔍 Validation Method:  
- Opened a few articles manually to check if extracted URLs exist in the text.  
- Verified extracted URLs against expected results.  
- Checked that no invalid links were included.  

### ✅ Validation Steps:  
1. Extracted URLs were saved to `results/links_extracted.txt`.  
2. Opened 3 sample articles manually and located the URLs in the text.  
3. Compared manual results with script output.  
4. Randomly tested extracted URLs to ensure they are functional.  

---

## 📌 Summary of Findings  
- The keyword cloud accurately reflects frequent words in the abstracts.  
- The figure count algorithm correctly identifies figures in the majority of cases.  
- The link extraction script retrieves URLs effectively but may require improvements for malformed links.  

For further improvements, automated unit tests will be developed to validate outputs systematically.  
