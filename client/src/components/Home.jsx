import React from "react";
import { Box, Grid2, Typography } from "@mui/material";
import CameraIcon from '@mui/icons-material/Camera';
import GitHubIcon from '@mui/icons-material/GitHub';

function Home(){

    return(
        <Box sx={{ flexGrow:1 }}>
            <Grid2 container spacing={2}>
                <Grid2 size={12}>
                    <Typography>timothy ryon</Typography>
                </Grid2>
                <Grid2 size={6}>
                    <Typography>01100011 01101111 01100100 01100101 </Typography>
                    <GitHubIcon />
                </Grid2>
                <Grid2 size={6}>
                    <Typography>Photography</Typography>
                    <CameraIcon />
                </Grid2>    
            </Grid2>
        </Box>
    );
}

export default Home;
