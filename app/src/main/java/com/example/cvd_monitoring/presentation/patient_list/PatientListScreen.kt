package com.example.cvd_monitoring.presentation.patient_list

import android.annotation.SuppressLint
import android.util.Log
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.runtime.Composable
import androidx.hilt.navigation.compose.hiltViewModel
import com.example.cvd_monitoring.presentation.patient_list.components.PatientListItem
import androidx.compose.runtime.remember
import androidx.core.os.bundleOf
import androidx.navigation.NavController
import com.example.cvd_monitoring.presentation.Screen
import com.example.cvd_monitoring.utils.Constants


@SuppressLint("StateFlowValueCalledInComposition")
@Composable
fun PatientListScreen(
    navController: NavController,
    viewModel: PatientListViewModel = hiltViewModel(),
) {
    val patientList = remember { viewModel.patientListResponse }
    val patients = patientList.value
    LazyColumn {
        items(patients) { patient ->
            PatientListItem(
                patient,
                onItemClick = {
                    navController.navigate(
                        Screen.UpdateDataPatient.route + "/${patient.slug}/data")

                }
            )
        }
    }
}



