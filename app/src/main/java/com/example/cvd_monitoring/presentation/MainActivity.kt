package com.example.cvd_monitoring.presentation

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.itemsIndexed
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.example.cvd_monitoring.domain.model.users.Patient
import com.example.cvd_monitoring.presentation.patient_list.PatientListScreen
import com.example.cvd_monitoring.presentation.patient_list.components.PatientListItem
import com.example.cvd_monitoring.presentation.sign_in.SignInScreen
import com.example.cvd_monitoring.presentation.sign_up.SignUpScreen
import com.example.cvd_monitoring.presentation.welcome.WelcomeScreen
import com.ramcosta.composedestinations.utils.composable
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
//            val navController = rememberNavController()
//
//            NavHost(
//                navController = navController,
//                startDestination = Screen.Home.route
//            ) {
//                composable(Screen.Home.route) {
//                    WelcomeScreen(navController=navController)
//                }
//
//                composable(Screen.SignUp.route) {
//                    SignUpScreen(navController=navController)
//                }
//
//                composable(Screen.SignIn.route) {
//                    SignInScreen(navController=navController)
//                }
//            }
           PatientListScreen()
        }
    }
}

