"use client"

import React from 'react';
import axios from 'axios';
import { useFormik } from 'formik';

interface FormValues {
    username: string;
    password: string;
}


const LoginForm: React.FC = () => {

    const onSubmit = async (values: FormValues) => {

        try{
            const response = await axios.post('http://127.0.0.1:5000/login', values)
            console.log(response)
        }

        catch(error) {
            console.error(error)
        }
        
      };
      
    const formik = useFormik({ initialValues: { username:"", password:""},
        validateOnBlur: true,
        onSubmit,})

    return (

        <form onSubmit={formik.handleSubmit}>
            <input
            placeholder="Username" 
            name='username'
            type="text"
            value={formik.values.username}
            onChange={formik.handleChange}/>

            <input 
            placeholder="Password" 
            name='password'
            type="password"
            value={formik.values.password}
            onChange={formik.handleChange} />
            <button type='submit'>Login</button>
            <button> Sign up</button>
        </form>
    );
};

export default LoginForm;