# GAN Implementation
 The GAN code that we referred to for our experiments can be found at <href>https://github.com/Zackory/Keras-MNIST-GAN</href>. For our implementation we modified the code to reflect the 4 different optimizers (Adam, Adagrad, SGD, RMSprop) that the experiment was performed on.

 The four ipynb files (adam, adagrad, sgd, rmsprop) have individual codes which produce outputs of their own and are recorded in respective files. Below I have listed the different files with the output files that have been produced by them.

 ### Adam Optimizer
  Code file -> adam.ipynb <br>
  Generated models folder -> models_adam <br>
  Loss graph at the end of 50 epochs -> images_adam <br>
  Loss and time per epoch -> adam_results

 ### Adagrad Optimizer
  Code file -> adagrad.ipynb <br>
  Generated models folder -> models_adagrad <br>
  Loss graph at the end of 50 epochs -> images_adagrad <br>
  Loss and time per epoch -> adagrad_results

 ### SGD Optimizer
  Code file -> sgd.ipynb <br>
  Generated models folder -> models_sgd <br>
  Loss graph at the end of 50 epochs -> images_sgd <br>
  Loss and time per epoch -> sgd_results

 ### RMSprop Optimizer
  Code file -> rmsprop.ipynb <br>
  Generated models folder -> models_rmsprop <br>
  Loss graph at the end of 50 epochs -> images_rmsprop <br>
  Loss and time per epoch -> rmsprop_results

 The code files contain the codes of each of the models. The generated models folder contain the models that are generated at at the 1st, 20th and 40th epochs. It records both the generator and discriminator models in this folder for each optimizer. The loss graph folder has the plot generated at the end of 50 epochs to show the losses of the two neural networks over the numerous epochs. The results file contains the generator loss, discriminator loss and the time taken at every epoch.