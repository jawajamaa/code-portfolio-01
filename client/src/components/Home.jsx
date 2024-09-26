import React from "react";
import { NavLink } from "react-router-dom";
import { useUrl } from "../providers/UrlContext";

import { Box, Grid2, Typography } from "@mui/material";
import CameraIcon from "@mui/icons-material/Camera";
import GitHubIcon from "@mui/icons-material/GitHub";
import LinkedInIcon from "@mui/icons-material/LinkedIn";

import bwHeadshot from "../../public/images/20240806_Ryon-Timothy_312_bw-sm.jpg";

function Home(){
    const { myGhUrl, myLinkedIn } = useUrl();
    
// give GH and aperture icons their own Grid locations for better spacing?

    return(
        <Box sx={{ flexGrow:1 }}>
            <Grid2 container spacing={2}>
                <Grid2 size={12}>
                    <Typography>timothy ryon</Typography>
                    <Typography>Developer</Typography>
                </Grid2>
                <Grid2 size={6}>
                    <img src = {bwHeadshot} 
                        width = "425"/>
                </Grid2>
                <Grid2 size={3}>
                    <NavLink to={`/code`}>
                        <Typography
                            className={"link"}>
                                01100011 01101111 01100100 01100101 
                        </Typography>
                    </NavLink>
                </Grid2>
                <Grid2 size={3}>
                    <a href = { myGhUrl }
                        target = "_blank"
                        className={"link"}>
                        <GitHubIcon />
                    </a>
                </Grid2>
                <Grid2 size={3}>
                    <a href = { myLinkedIn }
                        target = "_blank"
                        className = {"link"}>
                            <LinkedInIcon />
                        </a>
                </Grid2>
                <Grid2 size={3}>
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
