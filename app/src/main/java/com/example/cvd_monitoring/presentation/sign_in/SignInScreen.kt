package com.example.cvd_monitoring.presentation.sign_in

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
import com.example.cvd_monitoring.domain.model.users.Auth


@Composable
fun SignInScreen(signInViewModel: SignInViewModel) {
    val emailState = signInViewModel.emailState.value
    val passwordState = signInViewModel.passwordState.value
    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {

        TextField(
            value = emailState.text,
            onValueChange = { signInViewModel.setEmailValue(it) },
            label = { Text("Email") },
            modifier = Modifier
                .fillMaxWidth()
                .padding(bottom = 8.dp)
        )

        TextField(
            value = passwordState.text,
            onValueChange = { signInViewModel.setPasswordValue(it) },
            label = { Text("Password") },
            modifier = Modifier
                .fillMaxWidth()
                .padding(bottom = 8.dp)
        )

        Button(
            onClick = {
                val user = Auth(
                    email = emailState.text,
                    password = passwordState.text
                )
                signInViewModel.authenticateUser(user)
            },
            modifier = Modifier.fillMaxWidth()
        ) {
            Text("Sign In")
        }
    }
}