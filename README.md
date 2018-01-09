# Deep Learning Notes & Projects

### Projects
1. [Use GAN to create new sigils](https://github.com/morganecf/deep-learning/tree/master/sigilizer)
2. [Analyze stories and generate new ones](https://github.com/morganecf/deep-learning/tree/master/stories)
3. [Pix2Pix](https://www.floydhub.com/morganeciot/projects/pix2pix) on FloydHub using [cityscapes data](https://www.floydhub.com/morganeciot/datasets/cityscapes), anime data, .... This uses a TensorFlow port of pix2pix found [here](https://github.com/affinelayer/pix2pix-tensorflow). 
```
# Train cityscapes model
floyd run --gpu --env tensorflow-1.4 --data morganeciot/datasets/cityscapes/1:input "bash train_cityscapes.sh"

# Create new dataset from output (ex: morganeciot/projects/pix2pix/5/output --> morganeciot/datasets/cityscapes/2)
# Then test cityscapes model using 2 mount points:
floyd run --gpu \
  --env tensorflow-1.4 \
  --data morganeciot/datasets/cityscapes/1:input \
  --data morganeciot/datasets/cityscapes/2:checkpoint \
  "bash test_cityscapes.sh"
 
# Alternatively could have directly used output of pix2pix job as second mount point
```

### Notebooks
1. [Deep learning with Keras](https://github.com/morganecf/deep-learning/tree/master/notebooks/keras-notebooks)
2. [Deep learning for NLP](https://github.com/morganecf/deep-learning/tree/master/notebooks/nlp)
3. [Miscellaneous](https://github.com/morganecf/deep-learning/tree/master/notebooks/misc)
