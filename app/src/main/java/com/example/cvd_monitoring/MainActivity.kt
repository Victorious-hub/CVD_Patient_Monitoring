package com.example.cvd_monitoring

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.viewModels
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.itemsIndexed
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.material3.TextField
import androidx.compose.runtime.Composable
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.example.cvd_monitoring.domain.model.users.Patient
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


@Composable
fun PatientList(patientList: List<Patient>) {
    LazyColumn {
        itemsIndexed(items = patientList) { index, item ->
            PatientListItem(patient = item)
        }
    }
}
