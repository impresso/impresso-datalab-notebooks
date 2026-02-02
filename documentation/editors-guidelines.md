# Impresso Datalab editor's guidelines

Editor’s procedures for each phase of the editorial pipeline:

<img width="1920" height="1080" alt="3" src="https://github.com/user-attachments/assets/ec88ec5d-1d4c-4d2a-b3c7-1942e7dccec6" />


## Phase 0: Notebook is under production
- The editor is responsible for getting in touch with the author and supporting them in the development of a new notebook for the Impresso Datalab. The editor should ensure the notebook fits the purpose of Datalab and that the topic has the potential of benefiting our users. 
- The editor should also advise the authors with regards to the use of our template. Share the template and make sure authors follow it. 
- Finally, the editor must create an issue on GitHub in the folder impresso-datalab-notebooks, assign the issue to themselves and the author (if internal contributor), assign the issue to the project ‘Impresso Interfaces Releases’, tag it as follows:
- **Status: In progress** (if notebook is momentaneously frozen, change status to ‘on hold’. If the notebook is totally abandoned, change status to ‘archived’. If the notebook is finalised and published, change it to ‘done’).
- **Progress: Phase 0: Notebook is under production** (this should be updated according to the next phases.
- **Visibility: Public** (if notebook is not planned to be shown on Datalab webpage, then change visibility to ‘hidden’.
- **Area: datalab**
- **Release:** (it depends if there is an expected project release)

## Phase 1: Initial edit
- After receiving the first draft of the notebook, the editor should run the entire notebook and test the code. It is important to make sure that it runs in both Google Colab and locally. Besides, the editor must provide feedback on the structure of the notebook and its content by adding comments to the file on pull-request using ReviewNB. Comments on code and a summary of the comments added to the file using ReviewNB should be included as a comment in the GitHub issue. 
- The editor should provide the author with a deadline to address the changes (either 1 or 2 weeks, depending on the complexity).

## Phase 2: Revision 1
At this phase, the editor is responsible for finding an internal reviewer (someone working at the Impresso project) to provide feedback on the notebook. After identifying a reviewer, the editor should assign them to the GitHub issue and share the reviewer guidelines A as a comment on the issue (suggestion of text below). 


> This notebook will be reviewed in Phase 2 by @github_user. Please, refer to the reviewer's guidelines below and add your feedback as a comment on this issue. Any further comments are also welcome!
> **Deadline for this task is the 4th of July 2025**. Please, let me know in case you need more time to complete your review. 
> Notebook file: https://github.com/impresso/impresso-datalab-notebooks/blob/main/starter/notebook-name.ipynb
> 
> Internal review:
> 1. Is the code consistent? Eg. Use of variables, formatting
> 2. Is the explanation of the code correct? Is there imprecise information? Could we expand it in some aspect you consider important to understand the code?
> 3. Are there any references to external resources that could enrich this notebook?
> 4. Is the information (text in markdown) contained in the NB enough to perform the proposed task? Is there something missing?
> 5. Do the objectives under 'what you will learn' match the content? Do we provide everything we promise in the objectives?


The editor should support the author to address the changes proposed in the peer-review. Again, the editor should propose a deadline of 1 or 2 weeks for the author to respond to the suggestions. 

## Phase 3: Revision 2
The editor must invite an external reviewer (someone who does not work closely with Impresso) to provide feedback on the notebook. After identifying an external reviewer, the editor should tag them in a comment to the GitHub issue and share the reviewer guidelines B. 

> This notebook will be reviewed in Phase 3 by @github_user. Please, refer to the reviewer's guidelines below and add your feedback as a comment on this issue. Any further comments are also welcome! Thanks very much for contributing to the Impresso project.
> Notebook file: https://github.com/impresso/impresso-datalab-notebooks/blob/main/starter/notebook-name.ipynb
> 
> External review:
> 1. Is it clear for you what the objective of this NB is?
> 2. Is it easy to identify whether this NB is relevant to you?
> 3. Is the NB written in a clear format/layout? Do the sections/titles make sense to you?
> 4. Is the information provided enough for you to understand the code?
> 5. Is there anything you would like further explanation (Eg. any unclear concept)?
> 6. Are you able to run every cell in the NB and understand its outputs using your own examples?
> 7. Can you imagine any use of this NB in your own research pipelines? What would make this notebook more relevant for your research and/or teaching?

The editor should support the author to address the changes proposed in the external peer-review and propose a deadline of 1 or 2 weeks for the author to respond to the suggestions. 

## Phase 4: Sustainability assessment

- Replace, whenever possible, links to external resources with their Internet Archive version. 
- Check requirements
- Link Notebook to other existing related resources (Eg. HF models, papers, etc.) 

## Phase 5: Publication

- Assign DOI (Zenodo - https://zenodo.org/communities/impresso)
- Add notebook to Impresso Zotero 

