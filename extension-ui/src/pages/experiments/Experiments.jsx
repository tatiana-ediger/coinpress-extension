import React, { useEffect, useState } from "react";
import { makeStyles } from '@material-ui/core/styles';
import axios from 'axios';
import { Button, FormControl, FormHelperText, Grid, Paper, TextField, Select, MenuItem } from "@material-ui/core";
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
    },
    loading: {
        margin: theme.spacing(2),
        width: '500px',
        height: '300px'
    }
  }));

// the issue: the lists are not equal?

export default function Operate() {
    const nOptions = {
        Small: [500, 750, 1000, 1250, 1500, 1750, 2000, 2250, 2500],
        Large: [2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    }
    const [graphData, setGraphData] = useState({n_values:[], private_losses:[], nonprivate_losses:[]});
    const [nValues, setNValues] = useState(nOptions["Small"])
    const [d, setD] = useState(5);
    const [iters, setIters] = useState(30);
    const [loading, setLoading] = useState(true);
    const [totalPrivacyBudget, setTotalPrivacyBudget] = useState(0.5)
    const [requestData, setRequestData] = useState({n_values: nValues, d:d, iters:iters, total_privacy_budget:totalPrivacyBudget});

    const classes = useStyles();



    useEffect(() => {
        async function getData() {
            try {
                setLoading(true);
                const response  = await axios.post(APP_URL+'/losses', requestData)
                const private_losses = response.data.excess_private_loss
                const nonprivate_losses = response.data.excess_nonprivate_loss
                const response_data = {n_values: nValues, private_losses, nonprivate_losses};
                setGraphData(response_data);
                setLoading(false);
            } catch(e) {
                console.log(e)
            }
        }
        getData();
    }, [requestData])

    function handleChangeNValues(value) {
        // console.log(value === )
        setNValues(nOptions[value])
    }
    
    return (
        <Grid container spacing={4}>
            <Grid item>
                <Paper>
                <form >
                    <FormControl className={classes.selectButton}>
                        <Select
                            labelId="demo-simple-select-label"
                            id="demo-simple-select"
                            defaultValue={"Large"}
                            onChange={event => handleChangeNValues(event.target.value)}
                            >
                            <MenuItem value={"Large"}>
                                {JSON.stringify(nOptions["Large"])} 
                            </MenuItem>
                            <MenuItem value={"Small"}>{JSON.stringify(nOptions["Small"])}</MenuItem>
                            {/* <MenuItem value={[2000,4000]}>2000,4000</MenuItem> */}
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
            {loading? <Paper className={classes.loading}>Loading...</Paper> : <Grid item>
                <Paper>
                <Graph data={graphData} />
                </Paper>
            </Grid>}
        </Grid>
    );

};