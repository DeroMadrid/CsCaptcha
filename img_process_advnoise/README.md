# Add random process and adversarial noise to csCAPTCHA images

After collect images from Internet, we: 

- Adding random image processing operation. 
- Adding adversarial noise.

## STEP 1: Adding random image processing operation

- This part of code is in `ImageProcessing/`.
1. Edit `challenge_path` and `out_path` in line 144 and 145 of `ImageProcessing/add_process.py`.
2. Execute the command
```
python ImageProcessing/add_process.py
```

## STEP 2: Adding adversarial noise

This part of the code refer to the paper:

**Nesterov Acceralated Gradient and Scale Invariance for Adversarial Attacks (ICLR2020)**

- This part of code is in `ImageAdversarialNoise/`.
1. Put all the images you need to add noise into a folder.
2. Call method `add_new_label()` in `ImageAdversarialNoise/tool.py` to extract new image classes from the challenge images, and save the result in `tmp.txt`.
3. Copy the contents of `tmp.txt` and add them to the end of the `ImageAdversarialNoise/cls_dict.py`.
4. Call method `create_csv()` in `ImageAdversarialNoise/tool.py` to generate a csv file.
5. Edit `input_dir`, `output_dir`, `f2l` in `ImageAdversarialNoise/si_ni_fgsm.py`. 
7. Execute the command
```
ImageAdversarialNoise/si_ni_fgsm.py
```

