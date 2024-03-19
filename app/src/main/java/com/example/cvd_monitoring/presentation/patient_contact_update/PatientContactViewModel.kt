package com.example.cvd_monitoring.presentation.patient_contact_update

import android.util.Log
import androidx.compose.runtime.State
import androidx.compose.runtime.mutableStateOf
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.cvd_monitoring.common.TextFieldState
import com.example.cvd_monitoring.domain.model.users.PatientContact
import com.example.cvd_monitoring.domain.model.users.PatientData
import com.example.cvd_monitoring.domain.use_case.patient_contact.PatientContactUseCase
import com.example.cvd_monitoring.domain.use_case.patient_data.PatientDataUseCase
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.launch
import javax.inject.Inject


@HiltViewModel
class PatientContactViewModel @Inject constructor(
    private val patientContactUseCase: PatientContactUseCase,
) : ViewModel(){
    private val _firstNameState = mutableStateOf(TextFieldState())
    val firstNameState: State<TextFieldState> = _firstNameState

    fun setFirstNameValue(value: String) {
        _firstNameState.value = firstNameState.value.copy(text = value)
    }

    private val _lastNameState = mutableStateOf(TextFieldState())
    val lastNameState: State<TextFieldState> = _lastNameState

    fun setLastNameValue(value: String) {
        _lastNameState.value = lastNameState.value.copy(text = value)
    }

    private val _emailState = mutableStateOf(TextFieldState())
    val emailState: State<TextFieldState> = _emailState

    fun setEmailValue(value: String) {
        _emailState.value = emailState.value.copy(text = value)
    }

    private val _mobileState = mutableStateOf(TextFieldState())
    val mobileState: State<TextFieldState> = _mobileState

    fun setMobileValue(value: String) {
        _mobileState.value = mobileState.value.copy(text = value)
    }

    fun updatePatientContact(slug: String) {
        val firstName = firstNameState.value.text
        val lastName = lastNameState.value.text
        val email = emailState.value.text
        val mobile = mobileState.value.text

        viewModelScope.launch {
            try {
                val createdUser = patientContactUseCase(mobile, firstName, lastName, email, slug)
                Log.d("SignUpViewModel", "Sign up successful: $createdUser")
            } catch (e: Exception) {
                val errorMessage = e.message.toString()
                Log.e("SignUpViewModel", "Sign up error: $errorMessage", e)
            }
        }
    }
}