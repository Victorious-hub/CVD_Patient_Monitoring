package com.example.cvd_monitoring.presentation.sign_up

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.material3.TextField
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.example.cvd_monitoring.domain.model.users.User


@Composable
fun SignUpScreen(signUpViewModel: SignUpViewModel) {
    val firstNameState = signUpViewModel.firstNameState.value
    val lastNameState = signUpViewModel.lastNameState.value
    val emailState = signUpViewModel.emailState.value
    val passwordState = signUpViewModel.passwordState.value
    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        TextField(
            value = firstNameState.text,
            onValueChange = {
                signUpViewModel.setFirstNameValue(it)
            },
            label = { Text("First Name") },
            modifier = Modifier
                .fillMaxWidth()
                .padding(bottom = 8.dp)
        )
        TextField(
            value = lastNameState.text,
            onValueChange = { signUpViewModel.setLastNameValue(it) },
            label = { Text("Last Name") },
            modifier = Modifier
                .fillMaxWidth()
                .padding(bottom = 8.dp)
        )
        TextField(
            value = emailState.text,
            onValueChange = { signUpViewModel.setEmailValue(it) },
            label = { Text("Email") },
            modifier = Modifier
                .fillMaxWidth()
                .padding(bottom = 8.dp)
        )

        TextField(
            value = passwordState.text,
            onValueChange = { signUpViewModel.setPasswordValue(it) },
            label = { Text("Password") },
            modifier = Modifier
                .fillMaxWidth()
                .padding(bottom = 8.dp)
        )

        Button(
            onClick = {
                val user = User(
                    first_name =  firstNameState.text,
                    last_name = lastNameState.text,
                    email = emailState.text,
                    password = passwordState.text
                )
                signUpViewModel.createPatient(user)
            },
            modifier = Modifier.fillMaxWidth()
        ) {
            Text("Sign Up")
        }
    }
}
