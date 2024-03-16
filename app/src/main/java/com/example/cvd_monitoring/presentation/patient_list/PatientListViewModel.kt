package com.example.cvd_monitoring.presentation.patient_list

import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.cvd_monitoring.domain.model.users.Patient
import com.example.cvd_monitoring.network.PatientApiService
import kotlinx.coroutines.launch

class PatientListViewModel : ViewModel() {

    var patientListResponse:List<Patient> by mutableStateOf(listOf())
    private var errorMessage: String by mutableStateOf("")
    fun getPatientList() {
        viewModelScope.launch {
            val apiService = PatientApiService.getInstance()
            try {
                val patientList = apiService.getPatientList()
                patientListResponse = patientList
            }
            catch (e: Exception) {
                errorMessage = e.message.toString()
            }
        }
    }
}