package com.example.cvd_monitoring.presentation.patient_list

import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.runtime.Composable
import com.example.cvd_monitoring.domain.model.users.Patient
import com.example.cvd_monitoring.presentation.patient_list.components.PatientListItem

@Composable
fun PatientListScreen(patients: List<Patient>) {
    LazyColumn {
        items(patients) { patient ->
            PatientListItem(patient)
        }
    }
}


