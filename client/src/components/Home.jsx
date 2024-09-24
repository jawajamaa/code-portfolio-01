import React from "react";
import { NavLink } from "react-router-dom";
import { useUrl } from "../providers/UrlContext";


import { Box, Grid2, Typography } from "@mui/material";
import CameraIcon from '@mui/icons-material/Camera';
import GitHubIcon from '@mui/icons-material/GitHub';

function Home(){
    const { myGhUrl } = useUrl();
    
// give GH and aperture icons their own Grid locations for better spacing?

    return(
        <Box sx={{ flexGrow:1 }}>
            <Grid2 container spacing={2}>
                <Grid2 size={12}>
                    <Typography>timothy ryon</Typography>
                    <Typography>Developer</Typography>
                </Grid2>
                <Grid2 size={6}>
                    <NavLink to={`/code`}>
                        <Typography
                            className={"link"}>
                                01100011 01101111 01100100 01100101 
                        </Typography>
                    </NavLink>
                    <a href = { myGhUrl }
                        target = "_blank"
                        className={"link"}>
                        <GitHubIcon />
                    </a>
                </Grid2>
                <Grid2 size={6}>
                    <Typography>Photography</Typography>
                    <NavLink
                        to = {`/photography`}
                        className={"link"}>
                        <CameraIcon />
                    </NavLink>
                </Grid2>    
            </Grid2>
        </Box>
    );
}

export default Home;
