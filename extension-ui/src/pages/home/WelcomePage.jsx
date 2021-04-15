import React from 'react';
import { makeStyles} from '@material-ui/core';

const useStyles = makeStyles(theme => ({
    embeddedWriteUp: {
        height: '100%',
        width: '100%'
    }
  }));

function WriteUp(){

    const classes = useStyles();

    return(
        <div>Welcome! You're in the right place if you'd like to learn more about <a href="https://arxiv.org/abs/2006.06618">CoinPress</a> and it's extension to privately solve Linear Regression!</div>
    )
}

export default WriteUp;