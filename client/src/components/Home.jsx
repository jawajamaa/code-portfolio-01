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
    backgroundColor: "#6a716a",
    ...theme.typography.body2,
    padding: theme.spacing(1),
    textAlign: "center",
    color: theme.palette.text.secondary,
    ...theme.applyStyles("dark", {
        backgroundColor: "dark",
    }),
}));

function Home(){
    const { myGhUrl, myLinkedIn } = useUrl();
    

    return(
        <Box sx={{ flexGrow:1 }}>
            <Grid2 container spacing={2}>
                <Grid2 size={12}>
                    <Item>
                        <Grid2 
                            container spacing={2}
                            display="flex"
                            alignItems="center"
                        >
                            <Grid2 size={{ xs: 6, md: 2 }} offset={{ xs: 3, md: 0 }}>
                                <a href = { myGhUrl }
                                    target = "_blank"
                                    className={"link"}>
                                <GitHubIcon />
                                </a>
                            </Grid2>
                            <Grid2 size={{ xs: 'grow', md: 4 }} offset={{ md: 2 }}>
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
                        <Grid2                                 
                            display="flex" 
                            alignIems="flex-end"
                            container spacing={6}>
                            <Grid2 size={12}>
{/* '01100011 01101111 01100100 01100101' is replaced with 'A little more about me' which takes you to the page fka 'Code' */}
                                <NavLink to={`/code`}>
                                    <Typography
                                        className={"link"}>
                                            01100011 01101111 01100100 01100101 
                                    </Typography>
                                </NavLink>
                            </Grid2>
                            <Grid2 size={12}>
                                <a href={resume} download="Ryon-Timothy_Resume">
                                    <IconLabelButton 
                                        icon={<DownloadIcon />}
                                        label="Download Resume"/>
                                </a>
                            </Grid2>
{/* add 'A little about me section; aperture icon gets moved to the bottom and 'photography' is removed?*/}
                            <Grid2 
                                display="flex" 
                                alignIems="flex-end" 
                                justify="flex-end" 
                                size={12} 
                                offset={{ md: 10 }}
                            >
                                {/* <Typography>Photography</Typography> */}
                                <NavLink
                                    to = {`/photography`}
                                    className={"link"}>
                                    <CameraIcon />
                                </NavLink>
                            </Grid2>
                        </Grid2>
                    </Item>
                </Grid2>
            </Grid2>    
        </Box>
    );
}

export default Home;
