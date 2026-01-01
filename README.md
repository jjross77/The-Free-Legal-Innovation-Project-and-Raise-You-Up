
All files and folders in this repository are protected under the Attribution-ShareAlike 4.0 International CC BY-SA 4.0 license. "You are free to:
Share — copy and redistribute the material in any medium or format for any purpose, even commercially.
Adapt — remix, transform, and build upon the material for any purpose, even commercially.
The licensor cannot revoke these freedoms as long as you follow the license terms.
Under the following terms:
Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
ShareAlike — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.
No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits."
https://creativecommons.org/licenses/by-sa/4.0/deed.en

Attribution-ShareAlike 4.0 International CC BY-SA 4.0
Deed
    
    
1. What I want Raise You Up to be. Make it a GitHub for solving world problems where everyone works together on a single page to solve a world problem like climate change submitting different plans that could be taken to solve these problems, and they could donate money to people working on a world problem page to take the plan into reality but having a million people working together on a single page and devising plans to solve a problem I think would change the world for the better and is the best thing ever.
 
2. What I want FLIP to be is a website where all the free technology lawyers or layman people could use is there so they could have legal services delivered at a more affordable amount. And it would provide free legal education and legal information on top of all available free resources on the internet in terms of Legal Tech that my web spyder would find.

3.	PORKBUN and Hostinger to set up the site online
paid for a domain for FLIP for 10 years with pork bun 
https://porkbun.com
Domain Name:  Freelegalproject.org
the password and login to the account 
domain is below so if you need to access
Porkbun login Rossgrove77@gmail.com
Password: Munchlax1!!!!

4. Go to domain management and change the DNS of FreelegalProject.org to the external IP address on Hostinger by hovering over freelegalproject.org on previous page.
you will have if you go with hostinger to host the site and get an external IP address from them to set for the DNS on that page I don’t have an account, but you would make one and then you would be good and pay the basic fees
https://www.hostinger.com/pricing

once you have a hosting service and have changed the domain name to the right external IP address you then need to get the website code running on hostinger computer. By copying it onto the remote server

5. First download DEBERTA from hugging face https://huggingface.co/microsoft/deberta-v3-base. For the rest of the NN in the pipeline you need to find the data then format it so it can train those neural networks. Repeat this process for all the neural networks. The law finder I used spacy https://spacy.io/usage/linguistic-features to find law data so when word vectors are put through it differentiates between law and not law, the non sentence finder differentiate between words you want or don’t want. To create the dataset for this one looks for useless words by looking at a document categorizing words as wanted or not wanted words. For part of speech use Spacy and train a neural network using their results In the pipeline by running over each sentence https://spacy.io/usage/linguistic-features. The code for case categorizing is in pipe_line_to_process_documents6 document.


APPENDIX A WHERE THE CODE IS ON GITHUB

Under the PSP API folder are all of my different ideas stored as functions to still be built and added to the problem-solving program under file psp_search_function_api_functions.py.

The PSP API on the raise you up site would generate all the documents you might need to fill out and create in your workflow and will also generate documents that are tangentially related to the task you are trying to solve, giving you a different way a task might be completed or a problem to be solved.

 The other part of the PSP API is that it would be able to tell you future actions you might wish to take based on your current positionality. The basic idea I had for this was looking at the stories of other people's lives on Wikipedia and then sorting these people to create a list of all relevant people on Wikipedia someone might look to decide on the next chapter of their life.  The program would suggest courses of action that you might wish to take, which are guided by objectives like helping the most people or making the most money. And using Wikipedia to accomplish the task.

The FLIP folder has a neural network to categorize sentences of law into the Fact, Issue, and Analysis groupings. You would run the neural network as an API and try to get other websites to use it as an API because it could help generate lists of issues an attorney might use to appeal a decision. It could be used to ensure you are really following the principle of "Stare Decisis" decisions and finding the precedents that best reflect your case because you could search the database for the closest matching factual sentences now that you have cateogrized them differently than other sentences in a legal decision.

The PSP API would work in the Django tailwind PSP website folder. The stack for the website is running nginx back end with DJANGO and tailwindcss. 

PS you are always loved.

APPENDIX B

You will need to create a Django site then you would add these files I attached in the email to it to get it to run replacing the basic ones that are loaded in by creating a Django app
https://docs.djangoproject.com/en/5.2/intro/install/
https://docs.djangoproject.com/en/5.2/intro/tutorial01/
https://docs.djangoproject.com/en/5.2/intro/tutorial02/
the above explains how to set up the Django site
The code to run is on dad’s hard drive at his place under the folder I think Kimlichcova on a blue hard drive I gave him which is just Megan’s moms last name I spelled wrong. That is where all the free legal project stuff is located. I will try to attach some of the other files in my email to you, but I don’t have access to those files otherwise
The Sparrow xlsx is the data to train a new Fact Issue Application NN model. If I didn’t save the other neural networks you will have to train them too, but the process Is straight forward to do this part.
 
 First download DEBERTA from hugging face https://huggingface.co/microsoft/deberta-v3-base. For the rest of the NN in the pipeline you need to find the data then format it so it can train those neural networks. Repeat this process for all the neural networks. The law finder I used spacy https://spacy.io/usage/linguistic-features to find law data so when word vectors are put through it differentiates between law and not law, the non sentence finder differentiate between words you want or don’t want. To create the dataset for this one looks for useless words by looking at a document categorizing words as wanted or not wanted words. For part of speech use Spacy and train a neural network using their results In the pipeline by running over each sentence https://spacy.io/usage/linguistic-features. The code for case categorizing is in pipe_line_to_process_documents6 document.






















