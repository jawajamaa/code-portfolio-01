import React, { useEffect, useState } from "react";
import { Box, Grid2, Typography } from "@mui/material";
import DownloadIcon from '@mui/icons-material/Download';

import BannerMe from "./BannerMe";
import IconLabelButton from "./styleNavMui/IconLabelButton";
import Item from "./Item";
import QuadTych from "../../public/documents/QuadPic_bw02.jpg";
import resume from "../../public/documents/Ryon-Timothy_Resume.pdf";
import { useUrl } from "../providers/UrlContext";

import "./AboutMe.css";

// Keep the resume download, but perhaps put a little more fun information here, and keep the splash/home page short and succinct and more 'professional'? And can add the quad-tich fun photos?  Maybe move the aperture logo and link here?  Again, keeping the splash page simple and extras here for anyone who takes the extra time to look further. and add the link to my 30 sec About me video for 'anyone who prefers to watch instead of read'
function AboutMe() {
    const{ aboutMeUrl, baseUrl } = useUrl();
    const[aboutMeText, setAboutMeText] = useState();

    useEffect(() => {
        fetch(baseUrl + aboutMeUrl)
            .then(r => r.json())
            .then(textData => {
                setAboutMeText(textData)
            });
    },[aboutMeUrl])

    console.log(aboutMeText);

    return(
        <Box sx={{ flexGrow:1 }}>
            <Grid2 container spacing={2}>
                <BannerMe />
                <Grid2 size={6}>
                    <Item>
                        <img src = {QuadTych} 
                            width = "425"/>
                    </Item>
                </Grid2>
                <Grid2 size={6}>
                    <Item>
                        <Grid2>
                        <Typography>01000001 00100000 01001100 01101001 01110100 01110100 01101100 01100101 00100000 01101101 01101111 01110010 01100101 00100000 01100001 01100010 01101111 01110101 01110100 00100000 01101101 01100101 00100001 </Typography>
                        </Grid2>
                        <Grid2>
                            <Typography>
                                A Little about Me!
                            </Typography>
                        </Grid2>
                        <Grid2 size={6}>
                            <a href={resume} download="Ryon-Timothy_Resume">
                                <IconLabelButton 
                                    icon={<DownloadIcon />}
                                    label="Download Resume"/>
                            </a>
                        </Grid2>
                    </Item>
                </Grid2>
            </Grid2>
        </Box>
    );
}

export default AboutMe;
