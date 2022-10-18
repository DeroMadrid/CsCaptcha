# CsCaptcha Generation Code

This the Generation Code for CsCaptcha.

## Project file description

`allimage/`：Store pictures of various categories.

`alltxt/`：Store the corresponding question text for each category.

`extend/`：Store the question text for COMET and CommonsenseQA.

`image/`：Store the generated CsCaptcha.

`question_text/`：Store the question text and answer for the generated CsCaptcha.

##  Two Method to generate CsCaptcha

* **Question selected in `alltxt/`**

1. Download images for each category `alltxt/`  in `allimage/`.

2. Modify the path in `CsCaptchaGenerate_12_more_results_only_imgs.py`

3. Execute the command 

   ```
   python CsCaptchaGenerate_12_more_results_only_imgs.py
   ```

* **Question selected in COMET and CommonsenseQA.**

1. No need to download images in advance, this method will download image online.
2. Modify the path in `NewCsCaptchaGenerate.py`
3. Execute the command 

   ```
   python NewCsCaptchaGenerate.py
   ```

## Other code description

* **`wl-conceptDemo.py`**

1. Description: extended question file in `alltxt/`.
2. Get the question text based on keywords in Concept Net. 

* **`cometDemo.py`**

1. Description: Convert the data in the COMET dataset to the required question text format.

2. Reserve the required questions, and generate corresponding questions based on keywords.

3. Each row of the COMET dataset is a triplet of data, divided into two keywords, and a relationship.

4. Generation rules：

   | relationship  |                  question                   |     answer      |
   | :-----------: | :-----------------------------------------: | :-------------: |
   | "HasProperty" |         "What is " + keyword2 + "?"         |    keyword1     |
   |  "ObjectUse"  |     "What is used to " + keyword2 + "?"     |    keyword1     |
   | "AtLocation"  |   "What can you see in " + keyword2 + "?"   |    keyword1     |
   |  "CapableOf"  | "What/Who is capable of " + keyword2 + "?"  |    keyword1     |
   |   "Causes"    |     "What can cause " + keyword2 + "?"      |    keyword1     |
   |   "Desires"   |  "What/Who will desire " + keyword2 + "?"   |    keyword1     |
   | "HasSubEvent" | "What has sub event like " + keyword2 + "?" |    keyword1     |
   |  "MadeUpOf"   |   "What is made up of " + keyword2 + "?"    |    keyword1     |
   | "NotDesires"  |  "What does not desires " + keyword2 + "?"  |    keyword1     |
   |    others     |               ignore this one               | ignore this one |

* **`commonsenseDemo.py`**

1. Description: convert the data in the CommonsenseQA dataset into the required question text format.
2. Obtain the question text and the question answer in each row of data.



