import React, { Component } from 'react';


class Products extends Component {
    render() {
        return (
            <div style={{ display: 'flex', justifyContent: 'center', padding: 30 }}>
                <div><h2>Your TileSet</h2>
                <iframe src="https://online.transerve.com/preview/6065b1188066f700252ed176?access_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiNjA2NTkzZDkxNzA2MzYwMDFlM2U0NGY0Iiwic2Vzc2lvbiI6IjYwNjU5NmVhNTgyNjFlMDA1ZDU2MmRhMiIsImlhdCI6MTYxNzI3NzIwOH0.4dyjn87WR01AtGkrRmNoX3FIW0XbKT6cQ5I_cgUw0XU" title="Published from Online Transerve Stack" width="1000" height="700"></iframe>
                </div>
            </div>
        );
    }
}

export default Products;