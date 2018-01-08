# Deep Learning Notes & Projects

### Projects
1. [Use GAN to create new sigils](https://github.com/morganecf/deep-learning/tree/master/sigilizer)
2. [Analyze stories and generate new ones](https://github.com/morganecf/deep-learning/tree/master/stories)
3. [Pix2Pix](https://www.floydhub.com/morganeciot/projects/pix2pix) on FloydHub using [cityscapes data](https://www.floydhub.com/morganeciot/datasets/cityscapes), anime data, .... This uses a TensorFlow port of pix2pix found [here](https://github.com/affinelayer/pix2pix-tensorflow). The commands to use the person2anime model:
```
# Train
floyd run --gpu --env tensorflow-1.4 --data morganeciot/datasets/person2anime/1:input "bash train_person2anime.sh"
# Test
floyd run --gpu --env tensorflow-1.4 --data morganeciot/datasets/person2anime/1:input "bash test_person2anime.sh"
```

### Notebooks
1. [Deep learning with Keras](https://github.com/morganecf/deep-learning/tree/master/notebooks/keras-notebooks)
2. [Deep learning for NLP](https://github.com/morganecf/deep-learning/tree/master/notebooks/nlp)
3. [Miscellaneous](https://github.com/morganecf/deep-learning/tree/master/notebooks/misc)
