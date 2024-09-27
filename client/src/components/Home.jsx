import React from "react";
import { NavLink } from "react-router-dom";
import { useUrl } from "../providers/UrlContext";

import { Box, Grid2, Paper, Typography } from "@mui/material";
import CameraIcon from "@mui/icons-material/Camera";
import DownloadIcon from '@mui/icons-material/Download';
import GitHubIcon from "@mui/icons-material/GitHub";
import LinkedInIcon from "@mui/icons-material/LinkedIn";
import { styled } from "@mui/material/styles";

import IconLabelButton from "./styleNavMui/IconLabelButton";
import bwHeadshot from "../../public/images/20240806_Ryon-Timothy_312_bw-sm.jpg";
import resume from "../../public/documents/Ryon-Timothy_Resume.pdf";

const Item = styled(Paper)(({ theme }) => ({
    backgroundColor: "#fff",
    ...theme.typography.body2,
    padding: theme.spacing(1),
    textAlign: "center",
    color: theme.palette.text.secondary,
    ...theme.applyStyles("dark", {
        backgroundColor: "#1a2027",
    }),
}));

function Home(){
    const { myGhUrl, myLinkedIn } = useUrl();
    

    return(
        <Box sx={{ flexGrow:1 }}>
            <Grid2 container spacing={2}>
                <Grid2 size={12}>
                    <Item>
                        <Grid2 container spacing={2}>
                            <Grid2 size={{ xs: 6, md: 2 }} offset={{ xs: 3, md: 0 }}>
                                <a href = { myGhUrl }
                                    target = "_blank"
                                    className={"link"}>
                                <GitHubIcon />
                                </a>
                            </Grid2>
                            <Grid2 size={{ xs: 'grow', md: 6 }} offset={{ md: 2 }}>
                                <Typography>timothy ryon</Typography>
                                <Typography>Developer</Typography>
                            </Grid2>
                            <Grid2 size={{ xs: 4, md: 2 }} offset={{ md: 'auto' }}>
                                <a href = { myLinkedIn }
                                    target = "_blank"
                                    className = {"link"}>
                                    <LinkedInIcon />
                                </a>
                            </Grid2>
                        </Grid2>
                    </Item>
                </Grid2>
                <Grid2 size={6}>
                    <Item>
                        <img src = {bwHeadshot} 
                            width = "425"/>
                    </Item>
                </Grid2>
                <Grid2 size={6}>
                    <Item>
                        <NavLink to={`/code`}>
                            <Typography
                                className={"link"}>
                                    01100011 01101111 01100100 01100101 
                            </Typography>
                        </NavLink>

                        <a href={resume} download="Ryon-Timothy_Resume">
                            <IconLabelButton 
                                icon={<DownloadIcon />}
                                label="Download Resume"/>
                        </a>


                        <Typography>Photography</Typography>
                        <NavLink
                            to = {`/photography`}
                            className={"link"}>
                            <CameraIcon />
                        </NavLink>
                    </Item>
                </Grid2>
            </Grid2>    
        </Box>
    );
}

export default Home;
