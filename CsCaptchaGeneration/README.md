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

