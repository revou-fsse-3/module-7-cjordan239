"use client"

import React from 'react';
import axios from 'axios';
import { useFormik } from 'formik';

interface FormRegisterValues {
    username: string
    email: string
    password: string
}

const RegisterForm: React.FC = () => {

    const onSubmit = async (values: FormRegisterValues) => {
        try {
            const response = await axios.post('http://127.0.0.1:5000/login', values)
            console.log(`Your username: ${values.username}  email: ${values.email} password: ${values.password}`, response)
        }

        catch(error) {
            console.error('API Error:', error);
        }
    }

    const formik = useFormik({initialValues: {username:"", email:"", password:""},
    validateOnBlur:true,
    onSubmit})
    
    return (
        <form onSubmit={formik.handleSubmit}>
            <input
            placeholder="Username" 
            name='username'
            type="text"
            value={formik.values.username}
            onChange={formik.handleChange}/>

            <input 
            placeholder="Email" 
            name='email'
            type="email"
            value={formik.values.password}
            onChange={formik.handleChange} />
            

            <input 
            placeholder="Password" 
            name='password'
            type="password"
            value={formik.values.password}
            onChange={formik.handleChange} />

            <button type='submit'>Sign up</button>
        </form>
    );
};

export default RegisterForm;