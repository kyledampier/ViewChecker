import React from "react";
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import Button from '@mui/material/Button';

import TextEncoder from "./TextEncoder";
import ThumbnailEncoder from "./ThumbnailEncoder";

function App() {
  return (
    <Container>
      <Grid container>

        <Grid item xs={12}>
          <h1>Hello World</h1>
        </Grid>

        <Grid item xs={12} lg={6}>
          <h2>Upload Thumbnail</h2>
          <ThumbnailEncoder onChange={(obj) => console.log(obj)}/>
        </Grid>

        <Grid item xs={12} lg={6}>
          <h2>Enter Title</h2>
          <Grid>
            <TextEncoder onChange={(obj) => console.log(obj)}/>
          </Grid>
          <Grid>
            <Button variant="contained">Save</Button>
          </Grid>
        </Grid>


      </Grid>
    </Container>
  );
}

export default App;
