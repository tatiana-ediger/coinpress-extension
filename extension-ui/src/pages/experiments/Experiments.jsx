import React, { useEffect, useState } from "react";
import { makeStyles } from '@material-ui/core/styles';
import axios from 'axios';
import { Button, FormControl, FormHelperText, Grid, InputLabel, Paper, TextField, Select, MenuItem } from "@material-ui/core";
import Graph from './components/Graph';


const APP_URL = "http://127.0.0.1:5000"

const useStyles = makeStyles((theme) => ({
    root: {
      '& .MuiTextField-root': {
        margin: theme.spacing(1),
        width: '25ch',
      },
    },
    selectButton: {
          margin: theme.spacing(1),
          width: '25ch'
      },
    submitButton: {
        '& .MuiButton-root': {
            margin: theme.spacing(2),
            width: '10ch',
        }
    }
  }));

export default function Operate() {
    const defaultNVal = [2000,4000,6000,8000,10000]

    const [graphData, setGraphData] = useState({n_values:[], private_losses:[], nonprivate_losses:[]});
    const [nValues, setNValues] = useState(defaultNVal)
    const [d, setD] = useState(5);
    const [iters, setIters] = useState(30);
    const [totalPrivacyBudget, setTotalPrivacyBudget] = useState(0.5)
    const [requestData, setRequestData] = useState({n_values: nValues, d:d, iters:iters, total_privacy_budget:totalPrivacyBudget});

    const classes = useStyles();

    useEffect(() => {
        async function getData() {
            try {
                const response  = await axios.post(APP_URL+'/losses', requestData)
                const private_losses = response.data.excess_private_loss
                const nonprivate_losses = response.data.excess_nonprivate_loss
                const response_data = {n_values: nValues, private_losses, nonprivate_losses};
                setGraphData(response_data);
            } catch(e) {
                console.log(e)
            }
        }
        getData();
    }, [requestData])
    
    return (
        <Grid container spacing={4}>
            <Grid item>
                <Paper>
                <form >
                    <FormControl className={classes.selectButton}>
                    <Select
                        labelId="demo-simple-select-label"
                        id="demo-simple-select"
                        displayEmpty
                        defaultValue={defaultNVal}
                        onChange={event => setNValues(event.target.value)}
                        >
                        <MenuItem value={defaultNVal}>
                            2000,4000,6000,8000,10000 
                        </MenuItem>
                        <MenuItem value={[50,100,200,500]}>50,100,200,500</MenuItem>
                        <MenuItem value={[2000,4000]}>2000,4000</MenuItem>
                    </Select>
                    <FormHelperText id="demo-simple-select-label">n values</FormHelperText>
                    </FormControl>
                </form>
                <form className={classes.root}>
                    <TextField 
                        helperText="d" 
                        id="standard-basic" 
                        value={d}
                        onChange={(event) => setD(event.target.value)}/>
                </form>
                <form className={classes.root}>
                    <TextField 
                        helperText="iterations" 
                        id="standard-basic" 
                        value={iters}
                        onChange={(event) => setIters(event.target.value)}/>
                </form>
                <form className={classes.root}>
                    <TextField 
                        helperText="total privacy budget" 
                        id="standard-basic" 
                        value={totalPrivacyBudget}
                        onChange={(event) => setTotalPrivacyBudget(event.target.value)}/>
                </form>
                <Button className={classes.submitButton} 
                        color='primary' size='small' 
                        variant='outlined'
                        onClick={(event => setRequestData({n_values: nValues, d:d, iters:iters, total_privacy_budget:totalPrivacyBudget}))}> 
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