package com.example.cvd_monitoring.presentation.patient_list

import android.annotation.SuppressLint
import android.util.Log
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.runtime.Composable
import androidx.hilt.navigation.compose.hiltViewModel
import com.example.cvd_monitoring.presentation.patient_list.components.PatientListItem
import androidx.compose.runtime.remember


@SuppressLint("StateFlowValueCalledInComposition")
@Composable
fun PatientListScreen(
    viewModel: PatientListViewModel = hiltViewModel(),
) {
    val patientList = remember { viewModel.patientListResponse }
    Log.d("PatientListViewModel", "Patient list fetched: ${patientList.value}")
    val patients = patientList.value
    LazyColumn {
        items(patients) { patient ->
            PatientListItem(
                patient,
                onItemClick = {

                }
            )
        }
    }
}



