import React from 'react';
import './App.css';
import { makeStyles, CssBaseline, AppBar, Toolbar, Typography } from '@material-ui/core';
import { Drawer } from '@material-ui/core';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import { MenuItem } from '@material-ui/core';
import Experiments from './pages/experiments/Experiments'
import Writeup from './pages/writeup/WriteUp';

const useStyles = makeStyles(theme => ({
  root: {
    display: 'flex',
  },
  appBar: {
    zIndex: theme.zIndex.drawer + 2,
  },
  drawer: {
    width: 240,
    flexShrink: 0,
  },
  drawerPaper: {
    width: 240,
  },
  content: {
    flexGrow: 1,
    padding: theme.spacing(3),
  },
  link: {
    textDecoration: 'none',
    color: 'black',
  },
  toolbar: theme.mixins.toolbar,
}));

const App = () => {
  const classes = useStyles();

  return (
    <Router>
        <div className={classes.root}>
          <CssBaseline />
          <AppBar className={classes.appBar}>
            <Toolbar>
            <Typography variant="h5">CoinPress Extension</Typography>
            </Toolbar>
          </AppBar>
          <Drawer className={classes.drawer}
            variant="permanent"
            classes={{
              paper: classes.drawerPaper,
            }}>
            <div className={classes.toolbar} />

            <Link className={classes.link} to='/interactive'>
              <MenuItem>Interactive</MenuItem>
            </Link>
            <Link className={classes.link} to='/writeup'>
              <MenuItem>Write-up</MenuItem>
            </Link>
          </Drawer>
          <main className={classes.content}>
            <div className={classes.toolbar} />
            <Route exact path="/">

            </Route>
            <Route path="/interactive">
              <div><Experiments/></div>
            </Route>
            <Route path="/writeup">
              <Writeup/>
            </Route>
          </main>
        </div >
    </Router>
  );
}

export default App;

