# CoinPress Extension

This code implements a private solution for linear regression, extending CoinPress private estimators for the mean and covariance, published here: https://arxiv.org/abs/2006.06618. All the code from the coin-press folder was forked from https://github.com/twistedcubic/coin-press, except for files starting with lin_reg*, and app.py which I added. I also added the code inside the extension-ui folder in order to interact with this algorithm, tweaking parameters. 

## Installation

Using this code requires various python installations:
```bash
pip install pytorch.torchvision
pip install numpy
pip install matplotlib
```


## Usage

To start the backend API, you must navigate to coin-press folder and run app.py.

```bash
python app.py
```

To start the UI, you must navigate into the extension-ui folder, and then run the following commands.

```bash
npm i
npm start
```

Then you should see the UI pop-up in your default browser and you can interact with this algorithm by tweaking parameters!