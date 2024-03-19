package com.example.cvd_monitoring.presentation

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
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
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.Text
import androidx.compose.material3.TextField
import androidx.compose.material3.TextFieldDefaults
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
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
import androidx.hilt.navigation.compose.hiltViewModel
import androidx.lifecycle.ViewModel
import androidx.navigation.NavType
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import androidx.navigation.navArgument
import com.example.cvd_monitoring.domain.model.users.Patient
import com.example.cvd_monitoring.presentation.patient_contact_update.PatientContactScreen
import com.example.cvd_monitoring.presentation.patient_data_update.PatientUpdateScreen
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
            val navController = rememberNavController()

            NavHost(
                navController = navController,
                startDestination = Screen.PatientList.route
            ) {
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
                composable(
                    route = Screen.PatientList.route
                ) {
                    PatientListScreen(navController)
                }
                composable(
                    route = "${Screen.UpdateDataPatient.route}/{slug}/data",
                    arguments = listOf(navArgument("slug") { type = NavType.StringType })
                ) {
                    PatientUpdateScreen(navController = navController)
                }

//                composable(
//                    route = "${Screen.UpdateContactPatient.route}/{slug}/contact",
//                    arguments = listOf(navArgument("slug") { type = NavType.StringType })
//                ) {
//                    PatientContactScreen(navController = navController)
//                }
            }
        }
    }
}

