import React from 'react';
import { makeStyles} from '@material-ui/core';

const useStyles = makeStyles(theme => ({
    embeddedWriteUp: {
        height: '500%',
        width: '100%'
    }
  }));

function WriteUp(){

    const classes = useStyles();

    return(
        <embed className={classes.embeddedWriteUp} src="writeup.pdf"/>
    )
}

export default WriteUp;