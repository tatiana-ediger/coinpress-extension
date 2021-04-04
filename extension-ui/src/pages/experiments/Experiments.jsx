import React, { useEffect, useState } from "react";
import { makeStyles } from '@material-ui/core/styles';
import axios from 'axios';
import { Button, Grid, Paper, TextField } from "@material-ui/core";
import Graph from './components/Graph';

const APP_URL = "http://127.0.0.1:5000"

const useStyles = makeStyles((theme) => ({
    root: {
      '& .MuiTextField-root': {
        margin: theme.spacing(1),
        width: '25ch',
      },
    },
    submitButton: {
        '& .MuiButton-root': {
            margin: theme.spacing(2),
            width: '10ch',
        }
    }
  }));

export default function Operate() {
    const [graphData, setGraphData] = useState({n_values:[], private_losses:[], nonprivate_losses:[]});
    const [nValues, setNValues] = useState([2000,4000,6000,8000,10000])
    const classes = useStyles();
    const newPost = {
        n_values: nValues,
        d: 10,
        iters: 10,
        total_privacy_budget: 0.5
      }

    useEffect(() => {
        async function getData() {
            try {
                const response  = await axios.post(APP_URL+'/losses', newPost)
                console.log(response.data)
                const private_losses = response.data.excess_private_loss
                const nonprivate_losses = response.data.excess_nonprivate_loss
                const response_data = {n_values: nValues, private_losses, nonprivate_losses};
                setGraphData(response_data);
                console.log(graphData)
            } catch(e) {
                console.log(e)
            }
        }
        getData();
    }, [])
    
    return (
        <Grid container spacing={3}>
            <Grid item>
                <Paper>
                <form className={classes.root} noValidate autoComplete="off">
                    <TextField helperText="d" id="standard-basic" />
                </form>
                <form className={classes.root}>
                    <TextField helperText="n values" id="standard-basic" />
                </form>
                <form className={classes.root}>
                    <TextField helperText="iterations" id="standard-basic" />
                </form>
                <form className={classes.root}>
                    <TextField helperText="total privacy budget" id="standard-basic" />
                </form>
                <Button className={classes.submitButton} 
                        color='primary' size='small' 
                        variant='outlined'> 
                    run experiment 
                </Button>
                </Paper>
            </Grid>
            <Grid item>
                <Paper>
                <Graph data={graphData} />
                </Paper>
            </Grid>
        </Grid>
    );

};