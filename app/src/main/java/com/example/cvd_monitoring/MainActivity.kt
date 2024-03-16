package com.example.cvd_monitoring

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.viewModels
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.itemsIndexed
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.KeyboardActions
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material.icons.Icons
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.material3.TextField
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.Color.Companion.Red
import androidx.compose.ui.graphics.RectangleShape
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontStyle
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.text.input.PasswordVisualTransformation
import androidx.compose.ui.text.input.VisualTransformation
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.cvd_monitoring.domain.model.users.Patient
import com.example.cvd_monitoring.domain.model.users.User
import com.example.cvd_monitoring.presentation.patient_list.PatientListViewModel
import com.example.cvd_monitoring.presentation.patient_list.components.PatientListItem
import com.example.cvd_monitoring.presentation.sign_in.SignInScreen
import com.example.cvd_monitoring.presentation.sign_in.SignInViewModel
import com.example.cvd_monitoring.presentation.sign_up.SignUpScreen
import com.example.cvd_monitoring.presentation.sign_up.SignUpViewModel

class MainActivity : ComponentActivity() {
    val patientViewModel by viewModels<PatientListViewModel>()
    val signUpViewModel by viewModels<SignUpViewModel>()
    val signInViewModel by viewModels<SignInViewModel>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
//            SignUpScreen(
//                signUpViewModel
//            )
            SignInScreen(
                signInViewModel
            )
        }
    }
}

@Preview(showSystemUi = true)
@Composable
fun SignInPage() {
    val emailState = remember {
        mutableStateOf("")
    }
    val passwordState = remember {
        mutableStateOf("")
    }
    val password by rememberSaveable {
        mutableStateOf("")
    }
    var passwordVisibility by remember {
        mutableStateOf(false)
    }
    val icon = if(passwordVisibility)
        painterResource(id = R.drawable.visible1)
    else
        painterResource(id = R.drawable.invisible)

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {

        TextField(
            value = emailState.value,
            onValueChange = { emailState.value = it },
            label = { Text("Email") },
            modifier = Modifier
                .fillMaxWidth()
                .padding(bottom = 8.dp)

        )

        TextField(
            value = passwordState.value,
            onValueChange = { passwordState.value = it },
            label = { Text("Password") },
            modifier = Modifier
                .fillMaxWidth()
                .padding(bottom = 8.dp),
            trailingIcon = {
                IconButton(onClick = {
                    passwordVisibility = !passwordVisibility
                }) {
                    Icon(
                        painter = icon,
                        contentDescription = null
                    )
                }
            },
            keyboardOptions = KeyboardOptions(
                keyboardType = KeyboardType.Password
            ),
            visualTransformation = if (passwordVisibility) VisualTransformation.None else PasswordVisualTransformation()
        )

        Button(
            onClick = {

            },
            modifier = Modifier.fillMaxWidth(),
            colors = ButtonDefaults.buttonColors(
                containerColor = Color(0xFFa5051f),
                contentColor = Color.White
            ),
            shape = RoundedCornerShape(10.dp)
        ) {
            Text("Sign In")
        }
    }
}

@Composable
fun PatientList(patientList: List<Patient>) {
    LazyColumn {
        itemsIndexed(items = patientList) { index, item ->
            PatientListItem(patient = item)
        }
    }
}
