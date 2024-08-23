# A Multiomics Investigation of Endocrine Resistance in Breast Cancer

Cancer is a leading cause of premature mortality worldwide, with Estrogen Receptor-positive (ER+) breast cancers representing the majority of cases. These cancers are typically treated with endocrine therapy; however, 30-50% of patients develop intrinsic or acquired resistance, and the underlying mechanisms remain poorly understood.

This thesis explores endocrine resistance through a multiomics approach. The research comprised three key components. First, a custom proof-of-concept multiomics model was developed and trained on post-treatment DNA methylation, oral, and stool metagenomics data to predict patients' responses to endocrine therapy. The model demonstrated exceptional performance, achieving an AUC of 0.99 and an accuracy of 95%. Among the individual classifiers, DNA methylation data was the most informative, while gut microbiota data, surprisingly, contributed the least, despite the well-established connection between gut microbiota and estrogen metabolism via the estrobolome.

Secondly, models were constructed using pre-treatment metagenomics data from ER+ breast cancer patients and age-matched controls to identify potential biomarkers. Although these models showed moderate performance, they highlighted several bacteria differentially abundant between cancer and control groups, with most being elevated in control patients.

Finally, clinical models were developed using a minimal set of pre-treatment features to predict early endocrine resistance. This model also performed impressively, with an AUC of 0.97 and an accuracy of 95% using an SVM trained on just five prognostic markers. Additionally, these markers demonstrated predictive power for long-term outcomes, predicting breast cancer mortality with an AUC of 0.85 and an accuracy of 79%.

![image](https://github.com/user-attachments/assets/a6f2581f-427c-4764-b732-50ae29229560)



