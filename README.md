# Deep Learning Notes & Projects

### Projects
1. [Use GAN to create new sigils](https://github.com/morganecf/deep-learning/tree/master/sigilizer)
2. [Analyze stories and generate new ones](https://github.com/morganecf/deep-learning/tree/master/stories)
3. [Pix2Pix](https://www.floydhub.com/morganeciot/projects/pix2pix) on FloydHub using [cityscapes data](https://www.floydhub.com/morganeciot/datasets/cityscapes), anime data, .... This uses a TensorFlow port of pix2pix found [here](https://github.com/affinelayer/pix2pix-tensorflow). 
```
# Train cityscapes model
floyd run --gpu \
  --env tensorflow-1.4 \
  --data morganeciot/datasets/cityscapes/1:input \
  "bash train_cityscapes.sh"

# Create new dataset from output (ex: morganeciot/projects/pix2pix/5/output --> morganeciot/datasets/cityscapes/2)
# Need to make sure path references in cityscapes_train/checkpoint point to checkpoint. They will automatically
# point to /output/ since that was the path in the job. I downloaded the output, changed the references in the
# checkpoint file from /output/ to /input/ (/output/ is reserved, so there's no way around this), reuploaded
# to the cityscapes dataset, and used this.

# Test cityscapes model
floyd run --gpu \
  --env tensorflow-1.4 \
  --data morganeciot/datasets/cityscapes/1:input \
  "bash test_cityscapes.sh"

# TODO: change pix2pix code to take training arg that will output checkpoint paths to a given dir. Then can directly
# use output of pix2pix job as second mount point (called checkpoint):

# Test cityscapes model using 2 mount points
floyd run --gpu \
  --env tensorflow-1.4 \
  --data morganeciot/datasets/cityscapes/1:input \
  --data morganeciot/datasets/cityscapes/2:checkpoint \
  "bash test_cityscapes.sh"
```

### Notebooks
1. [Deep learning with Keras](https://github.com/morganecf/deep-learning/tree/master/notebooks/keras-notebooks)
2. [Deep learning for NLP](https://github.com/morganecf/deep-learning/tree/master/notebooks/nlp)
3. [Miscellaneous](https://github.com/morganecf/deep-learning/tree/master/notebooks/misc)
