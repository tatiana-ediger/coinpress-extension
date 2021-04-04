import React, { useState } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

const Graph = (props) => {

    const data = generateData(props.data)

    return (
    //   <ResponsiveContainer width="100%" height="100%">
        <LineChart
          width={500}
          height={300}
          data={data}
          margin={{
            top: 5,
            right: 30,
            left: 20,
            bottom: 5,
          }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line name="Private Losses" type="monotone" dataKey="pl" stroke="#8884d8" activeDot={{ r: 8 }} />
          <Line name="Non-private Losses" type="monotone" dataKey="npl" stroke="#82ca9d" />
        </LineChart>
    //   </ResponsiveContainer>
    );
};

function generateData(data) {
    const n_values = data.n_values
    const private_losses = data.private_losses;
    const nonprivate_losses = data.nonprivate_losses;

    const rechart_data = [];

    for (let i = 0; i < n_values.length; i++) {
        rechart_data.push({name: n_values[i], pl: private_losses[i], npl: nonprivate_losses[i]})
    };

    return rechart_data;
};

export default Graph;