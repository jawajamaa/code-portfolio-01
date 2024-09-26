import * as React from 'react';
import Button from '@mui/material/Button';
// import DeleteIcon from '@mui/icons-material/Delete';
// import SendIcon from '@mui/icons-material/Send';
// import Stack from '@mui/material/Stack';

export default function IconLabelButton({ icon, type = "submit", label = "Submit"}) {
  return (
      <Button 
        variant="contained" 
        endIcon={icon}
        type={type}
        >
        {label}
      </Button>
  );
}
